"use client";

import { Skeleton } from "@/components/ui/skeleton";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/Table";

export function DataTableSkeleton({
    rowCount = 5,
    columnCount = 6,
}: {
    rowCount?: number;
    columnCount?: number;
}) {
    return (
        <div className="w-full">
            <div className="flex items-center justify-between py-4">
                <Skeleton className="h-10 w-64" />
                <Skeleton className="h-10 w-40" />
            </div>
            <div className="rounded-md border">
                <Table>
                    <TableHeader>
                        <TableRow>
                            {Array.from({ length: columnCount }).map((_, i) => (
                                <TableHead key={i}>
                                    <Skeleton className="h-5 w-20" />
                                </TableHead>
                            ))}
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {Array.from({ length: rowCount }).map((_, i) => (
                            <TableRow key={i}>
                                {Array.from({ length: columnCount }).map((_, j) => (
                                    <TableCell key={j}>
                                        <Skeleton className="h-5 w-full" />
                                    </TableCell>
                                ))}
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </div>
            <div className="flex items-center justify-end space-x-2 py-4">
                <Skeleton className="h-8 w-24" />
                <Skeleton className="h-8 w-24" />
            </div>
        </div>
    );
}
